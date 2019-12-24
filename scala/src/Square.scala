object Square {

  def squareSum(xs: List[Int]): Int =
    (for (i <- xs) yield i**2).sum
}
