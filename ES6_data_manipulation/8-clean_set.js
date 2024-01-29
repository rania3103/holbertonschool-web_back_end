export default function cleanSet(set, startString) {
  return [...set].reduce((acc, str) => {
    let setFiltered = acc;
    if (str && str.startsWith(startString) && startString !== '') {
      setFiltered += `${str.slice(startString.length)}-`;
    }
    return setFiltered;
  }, '').slice(0, -1);
}
