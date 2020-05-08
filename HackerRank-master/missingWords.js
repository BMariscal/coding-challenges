// Question - 1
//
//Missing Words
//
//Given two strings, one is a subsequence if all of the elements of the
//ﬁrst string occur in the same order within the second string. They do
//not have to be contiguous in the second string, but order must be
//maintained. For example, given the string 'I like cheese', the words ('I',
//'cheese') are one possible subsequence of that string. Words are space
//delimited.
//
//Given two strings, s and t, where t is a subsequence of s, report the
//words of s, missing in t (case sensitive), in the order they are missing.
//
//Example
//
//s = 'I like cheese'
//t = 'like'
//
//Then 'like' is the subsequence, and ['I', 'cheese'] is the list of missing
//words, in order.
//
//Function Description
//
//Complete the function missingWords in the editor below.
//
//missingWords has the following parameter(s):
//
//string s:  a sentence of space-separated words
//string t:  a sentence of space-separated words
//
//Returns:
//
//string[i]: an array of strings that contains all words in s that are
//missing from t, in the order they occur within s
//
//Constraints
//
//Strings s and t consist of English alphabetic letters (i.e., a−z and
//
//A−Z), dash '-', and spaces only.
//
//All words are delimited by a space
//
//1 ≤ |t| ≤ |s| ≤ 10⁶
//
//1 ≤ length of any word in s or t ≤ 15
//
//It is guaranteed that string t is a subsequence of string s.
//
//Input Format for Custom Testing
//
//Input from stdin will be processed as follows and passed to the
//function.
//
//The ﬁrst line contains a string s.
//The ﬁrst line contains a string t.
//
//
//Sample Case 0
//Sample Input
//
//Help
//
//1/2
//
//
//STDIN
//
//4/30/2020                       2/F2u0n2c0tiEonnablement Series HackerRank
//Question | Programming problems and challenges | HackerRank
//
//I am using HackerRank to improve programming   →
//s = 'I am using HackerRank to improve
//programming'
//
//am HackerRank to improve                        →
//t = 'am HackerRank to improve'
//
//Sample Output
//
//I
//
//using
//programming
//
//Explanation
//
//The missing words are:
//
//1. I
//
//2. using
//
//3. programming
//
//Add these words in order to the array ["I", "using", "programming"],
//then return this array as the answer.



function missingWords(s, t){
    t = t.split(" ")
    s = s.split(" ")
    let res = []

    let t_words = new Set()
    for (let i=0;i < t.length; i++){
        t_words.add(t[i])

    }
    for (let i=0;i < s.length; i++){
        if (!t_words.has(s[i])){
            res.push(s[i])
        }
    }

    return res

}

let s ='I like cheese'
let t = 'like'
let a = missingWords(s, t)
console.log(a)