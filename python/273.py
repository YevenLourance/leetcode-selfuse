class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
        words = []

        i = 0
        while num>0:
            remainder = num%1000
            str_number = str(remainder)
            tmp_words = []
            if len(str_number)==3:
                tmp_words.append(ones[int(str_number[0])])
                tmp_words.append("Hundred") 

            if len(str_number)>=2:
                if str_number[-2] == '1':
                    tmp_words.append(teens[int(str_number[-1])]) 
                else:
                    tmp_words.append(tens[int(str_number[-2])]) 
                    tmp_words.append(ones[int(str_number[-1])])

            if len(str_number)==1:
                tmp_words.append(ones[int(str_number[-1])]) 

            if i > 0 and len(" ".join(filter(None, tmp_words)))>0:
                tmp_words.append(suffixes[i])

            words = tmp_words + words
            num = num//1000
            i = i+1

        return " ".join(filter(None, words))
        