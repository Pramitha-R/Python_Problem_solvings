


def solution(A, B, C):
    rt = ""

    while (0 < A or 0 < B or 0 < C ) :
        if (A<B and C<B):
            for i in range(2):
                if (0 < B):
                    rt = rt +'b'
                    B -= 1
            if(A<C):
                for i in range(2):
                    if (0 < C):
                        rt = rt +'c'
                        C -= 1
                if (0 < A):
                    rt = rt +'a'
                    A -= 1
            if(C<A):
                for i in range(2):
                    if (0 < A):
                        rt = rt +'a'
                        A -= 1
                if (0 < C):
                    rt = rt +'c'
                    C -= 1
            
        elif (C<A and B<A):
            for i in range(2):
                if (0 < A):
                    rt = rt +'a'
                    A -= 1
                
            if(B<C):
                for i in range(2):
                    if (0 < C):
                        rt = rt +'c'
                        C -= 1
                if (0 <B):
                    rt = rt +'b'
                    B -= 1
            if(C<B):
                for i in range(2):
                    if (0 < B):
                        rt = rt +'b'
                        B -= 1
                if (0 < C):
                    rt = rt +'c'
                    C -= 1


        elif (A<C and B<C):
            for i in range(2):
                if (0 < C):
                    rt = rt +'c'
                    C-= 1
                
            if(B<A):
                for i in range(2):
                    if (0 < A):
                        rt = rt +'a'
                        A -= 1
                if (0 <B):
                    rt = rt +'b'
                    B -= 1
            if(A<B):
                for i in range(2):
                    if (0 < B):
                        rt = rt +'b'
                        B -= 1
                if (0 < A):
                    rt = rt +'a'
                    A -= 1
            
    print(rt)
            

        # More 'a', append "aab"
        
    # Implement your solution here
    pass


solution(2,3,1)