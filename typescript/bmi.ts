export function bmi(weight: number, height: number): string {
  const bmi = weight/height**2
  if (bmi <= 18.5) {
    return "Underweight"
  } else if (bmi <= 25.0) {
    return  "Normal"
  } else if (bmi <= 30.0) {
    return "Overweight"
  } else {
    return "Obese" 
  }
  throw new Error("The method or operation is not implemented.");
}
