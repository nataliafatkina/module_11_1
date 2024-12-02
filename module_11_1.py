import pandas as pd
import matplotlib.pyplot as plt

# === Pandas ===
dataset = pd.read_csv('gym_members_exercise_tracking.csv')

# Выбираем только некоторые столбцы для создания анализа
data = dataset[['Age', 'Weight (kg)', 'Max_BPM', 'Workout_Type']].copy()

# Создаем категории по возрастам
data['Age_Category'] = pd.cut(data['Age'], bins=[0, 19, 29, 39, 49, 100], labels=['до 20', 'до 30', 'до 40', 'до 50', '50 и старше'])

# Наиболее популярные тренировки в каждой возрастной категории
popular_workouts = data.groupby('Age_Category', observed=True)['Workout_Type'].agg(lambda x: x.mode().iloc[0])
print("Самые популярные тренировки по возрастным категориям:")
print(popular_workouts)

# Ранжирование по частоте типа тренировок относительно всех тренировок
workout_counts = data['Workout_Type'].value_counts()
workout_percentages = (workout_counts / workout_counts.sum()) * 100
print("Распределение типа тренировок (% от общего числа тренировок):")
print(round(workout_percentages, 2))

# Средний возраст участника по каждому типу тренировок
avg_age_by_workout = data.groupby('Workout_Type')['Age'].mean()
print("\nСредний возраст участника по виду тренировки:")
print(avg_age_by_workout)

# Средний вес по каждой возрастной категории
popular_workouts = data.groupby('Age_Category', observed=True)['Weight (kg)'].mean()
print("\nСредний вес по возрастным категориям:")
print(popular_workouts)

# Средний максимальный пульс по каждой возрастной категории
avg_max_bpm_by_age_category = data.groupby('Age_Category', observed=True)['Max_BPM'].mean()
print("\nСредний максимальный пульс по возрастным категориям:")
print(avg_max_bpm_by_age_category)

# Процент каждой возрастной группы относительно всех спортсменов
category_counts = data['Age_Category'].value_counts(sort=False)


# === Matplotlib ===
plt.figure(figsize=(10,5))

# Визуализация данных распределения тренировок
plt.subplot(1,2,1)
workout_percentages.plot(kind='pie', autopct='%1.1f%%',
                         title='Распределение типа тренировок')
plt.ylabel('')

# Визуализация данных распределения возрастных групп
plt.subplot(1,2,2)
avg_age_by_workout.plot(kind='bar', title='Средний возраст по типам тренировок')
plt.ylim(15, 50)
plt.xlabel('Тип тренировок')
plt.ylabel('Возрастная группа')

plt.tight_layout()
plt.show()
