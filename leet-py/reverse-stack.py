stk = [5, 3, 2, 1, 6, 4, 3, 2, 1]

def insert_at_bottom(st, v):
    if not st:
        st.append(v)
    else:
        temp = st.pop()
        insert_at_bottom(st, v)
        st.append(temp)

def reverse_stk(st):
    if not st:
        return
    else: 
        temp = st.pop()
        reverse_stk(st)
        insert_at_bottom(st, temp)
    
# reverse_stk(stk)
# print(stk)
        

def sort_stk(st):
    if not st: 
        return st
    else:
        temp = st.pop()
        sort_stk(st)
        insert_sorted(st, temp)

def insert_sorted(st, v):
    if not st:
        st.append(v)
    elif st[-1] <= v:
        st.append(v)
    else:
        temp = st.pop()
        insert_sorted(st, v)
        st.append(temp)

sort_stk(stk)
print(stk)

        

