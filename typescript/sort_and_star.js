function twoSort(s) {
  s.sort()
  return s[0].replace(/(.)(?=.)/g, "$1***");
}

/*
function twoSort(s) {
  return s.sort()[0].split('').join('***');
}
*/
