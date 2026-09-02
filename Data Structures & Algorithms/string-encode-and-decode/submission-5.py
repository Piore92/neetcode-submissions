class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_str = ""
        for string in strs:
            combined_str = combined_str + str(len(string))
            combined_str = combined_str + ('&')
            combined_str = combined_str + string
        return combined_str


    def decode(self, s: str) -> List[str]:

        decoded_strings_list = []

        cntr = 0
        encoded_string_start = 0
        while(cntr < len(s)):
            if(s[cntr] == '&'):

                string_len = int(s[encoded_string_start:cntr])
                cntr+=1
                encoded_string_start = cntr + string_len

                decoded_strings_list.append(s[cntr:encoded_string_start])
                cntr=encoded_string_start
            cntr+=1

        return decoded_strings_list