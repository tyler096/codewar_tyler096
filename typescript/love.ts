/*export function howMuchILoveYou(petals: number): string{
  if (petals === 1) {
    return "I love you"
  } else if (petals === 2) {
    return "a little"
  } else if (petals === 3) {
    return "a lot"
  } else if (petals === 4) {
    return "passionately"
  } else if (petals === 5) {
    return "madly"
  } else if (petals === 6) {
    return "not at all"
  } else {
    return "I love you"
  }
}
 */
export function howMuchILoveYou(petals: number): string | undefined{
 if(petals > 0){
    switch(petals % 6){
      case 1:
        return "I love you"
      case 2:
        return "a little"
      case 3:
        return "a lot"
      case 4:
        return "passionately"
      case 5:
        return "madly"
      case 0:
        return "not at all"
    }
  }
  return undefined
}
