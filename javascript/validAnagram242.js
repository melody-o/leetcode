/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let obj = {};
    let str1 = s.toLowerCase();
    let str2 = t.toLowerCase();

    for (char of str1){
        if (!(char in obj)){
            obj[char] = 0
        }
        obj[char] += 1
    }

    for (char of str2){
        if (char in obj){
            obj[char] -= 1
        }else return false
    }

    for (char in obj){
        if (obj[char] != 0) return false
    }

    return true
};
