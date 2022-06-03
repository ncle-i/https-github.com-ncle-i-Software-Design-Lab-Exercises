def max(data,n):

    if n==1:

        return data[0]

    else:

        m=max(data,n-1)

        return data[n-1] if(data[n-1]>m) else m
