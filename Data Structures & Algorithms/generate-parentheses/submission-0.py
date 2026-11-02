class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def gen(op, cl, res):
            if op == cl == n:
                result.append(''.join(res))
            
            if op < n:
                res.append('(')
                gen(op+1,cl,res)
                res.pop()

            if op > cl:
                res.append(')')
                gen(op,cl+1,res)
                res.pop()
        
        gen(0,0,[])

        return result