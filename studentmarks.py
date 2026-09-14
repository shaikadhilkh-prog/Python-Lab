def calculate_stats(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    highest = max(marks) if marks else 0
    lowest = min(marks) if marks else 0
    return total, average, highest, lowest

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    students = []
    try:
        num_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid input. Please enter an valid number.")
        return
    
    for i in range(num_students):
        name = input(f"Enter name for student {i + 1}: ").strip()

        marks_input = input(f"Enter marks obtained in subjects (comma-separated): ")
        marks_input = marks_input.replace(' ', ',')
        try:
            marks = [float(m) for m in marks_input.split(',')]
        except ValueError:
            print("Invalid input format. Skipping this student record.")
            continue

        if not marks:
            print("No marks entered. Skipping this student record.")
            continue

        total, average, highest, lowest = calculate_stats(marks)
        grade = determine_grade(average)

        students_record = {
            'name': name,
            'total': total,
            'average': average,
            'highest': highest,
            'lowest': lowest,
            'grade': grade
        }
        students.append(students_record)

    if not students:
        print("No valid student records to display.")
        return

    students.sort(key=lambda x: x['total'], reverse=True)

    print("\n" + "=" * 65)
    print(f"{'Name':<15} {'Total':<10} {'Average':<10} {'Highest':<10} {'Lowest':<10} {'Grade':<5}")
    print("=" * 65)
    for s in students:
        print(f"{s['name']:<15} {s['total']:<10.2f} {s['average']:<10.2f} {s['highest']:<10.2f} {s['lowest']:<10.2f} {s['grade']:<5}")
    print("=" * 65)

if __name__ == "__main__":
    main()