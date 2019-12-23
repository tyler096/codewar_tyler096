object CenturyYear {
  def centuryFromYear(year: Int): Int =
    (year - 1) / 100 + 1
}