#pragma once

#define C_ARRAY_LENGTH(A) (sizeof(A) / sizeof(*(A)))

#define PP_STR(M)         _PP_STR(M)
#define PP_CAT(A, B)      _PP_CAT(A, B)
#define PP_MAX(A, B)      (A > B ? A : B)
#define PP_MIN(A, B)      (A < B ? A : B)

#define ARG_COUNT(...)    _ARGCNT1(__VA_ARGS__)
#define ABS(V)            PP_MAX(V, -(V))

#define in_range(VAR, ...) PP_CAT(_IN_RANGE_, ARG_COUNT(__VA_ARGS__))(VAR, __VA_ARGS__)

#define LINE(...) PP_CAT(_LINE_, ARG_COUNT(__VA_ARGS__))(__VA_ARGS__)

/* Private: */

#define _ARGCNT1(...) _ARGCNT2(IGNORED, ##__VA_ARGS__, _ARGCNT4)
#define _ARGCNT2(...) _ARGCNT3(__VA_ARGS__)
#define _ARGCNT3(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG,n,...) n
#define _ARGCNT4 32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0

#define _PP_STR(M) #M
#define _PP_CAT(A, B) A##B

#define _IN_RANGE_1(VAR, END) _IN_RANGE_2(VAR, 0, END)
#define _IN_RANGE_2(VAR, BEGIN, END) _IN_RANGE_3(VAR, BEGIN, END, 1)
#define _IN_RANGE_3(VAR, BEGIN, END, STEP) VAR = BEGIN ; VAR < END ; VAR += STEP

#define _LINE_1(A)          _LINE_2(A, 0)
#define _LINE_2(A, B)       _LINE_3(A, B, 0)
#define _LINE_3(A, B, C)    _LINE_4(A, B, C, 0)
#define _LINE_4(A, B, C, D) (uint8_t)((A << 4) + (B << 3) + (C << 2) + (D << 1))
