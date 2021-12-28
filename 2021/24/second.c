long int monad(char input[14]);

# define LOOP(V) V = 0; while (++V < 10) {
# define LETTERS a,b,c, d,e,f, g,h,i, j,k,l, m,n

int main()
{
    char LETTERS;

    LOOP(a)
    LOOP(d)
    LOOP(f)
    LOOP(h)
    LOOP(j)
    LOOP(l)
    LOOP(m)
    LOOP(g)
    LOOP(i)
    LOOP(c)
    LOOP(k)
    LOOP(e)
    LOOP(n)
    LOOP(b)
//        printf("%i%i%i%i%i%i%i%i%i%i%i%i%i%i\n", LETTERS);
    if (!monad((char[14]){LETTERS}))
    {
        printf("%i%i%i%i%i%i%i%i%i%i%i%i%i%i\n", LETTERS);
        return 0;
    }
    }}}}}}}}}}}}}}
}
