export class Kata {
    public static bonusTime(salary:number, bonus:boolean):string {
        if (bonus) {
            return "\u00A3" + (salary * 10).toString()
        } else {
            return "\u00A3" + (salary).toString()
        }
    }
}

/*
export class Kata {
    public static bonusTime(salary:number, bonus:boolean):string {
      return `£${salary * (bonus ? 10 : 1)}`;
    }
}
*/
