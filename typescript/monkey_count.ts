export function monkeyCount(n: number) {
  return [...Array(n).keys()].map((i,v) => ++i)
}
