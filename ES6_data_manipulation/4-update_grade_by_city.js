export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city && newGrades
    .map((studentGrade) => studentGrade.studentId).includes(student.id))
    .map((elem) => ({ ...elem, grade: newGrades.grade ? newGrades.grade : 'N/A' }));
}
