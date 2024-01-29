export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  } else {
    map.forEach((v, k) => {
      if (v === 1) {
        map.set(k, 100);
      }
    });
  }
}
