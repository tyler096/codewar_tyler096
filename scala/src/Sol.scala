object Sol {
  def evenOrOdd(number: Int): String = {
    if (number % 2 == 0) {
      "Even"
    } else {
      "Odd"
    }
  }
}


/*
object Sol {

  def evenOrOdd(number: Int): String = number % 2 match {
    case 0 => "Even"
    case _ => "Odd"
    }
}
*/