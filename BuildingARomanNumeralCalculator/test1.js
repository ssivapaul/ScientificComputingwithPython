function toRoman(num) {
  const romanNumerals = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];
  let result = "";
  for (let [value, numeral] of romanNumerals) {
    console.log("Value: ", value);
    console.log("Num: ", num);
    while (num >= value) {
      result += numeral;
      console.log("Result: ", result);
      num -= value;
    }
  }
  return result;
}

console.log(toRoman(35));
