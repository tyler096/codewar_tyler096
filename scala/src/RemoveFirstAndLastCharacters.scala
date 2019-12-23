object RemoveFirstAndLastCharacters {
  def removeChars(s: String): String = {
    if (s.length == 1) {
      "expected"
    }
    else {
      s.slice(1, s.length -1)
    }
  }
}


/*object RemoveFirstAndLastCharacters {
  def removeChars(s: String): String = {
    s.tail.init
  }
}
*/