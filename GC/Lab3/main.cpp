#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

struct Punct {
    float x, y;
    Punct(float x, float y) : x(x), y(y) {};
    Punct() {};
};

struct Dreapta {
    int a, b, c;
    Dreapta(int a, int b, int c) : a(a), b(b), c(c) {};
};

void read(vector<Punct> &v) {
    int x, y;
    for(int i=0; i<4; i++) {
        scanf("%d %d",&x,&y);
        v.push_back(Punct(x, y));
    }
}

Dreapta computeSegment(Punct A, Punct B) {
    int a, b, c;

    a = B.y - A.y;
    b = A.x - B.x;
    c = A.x*A.y + A.y*B.x - A.x*B.y - A.x*A.y;

    return Dreapta(a, b, c);
}

int linesIntersection(Dreapta d1, Dreapta d2, Punct &p) {
    int detA = (d1.a*d2.b - d1.b*d2.a);

    if(detA != 0) {
        float x = (float)(d2.c*d1.b - d1.c*d2.b) / (d1.a*d2.b - d2.a*d1.b);
        float y = (float)( -d1.c - d1.a*x) / d1.b;
        p = Punct(x, y);

        return 0; /// intersectia intr-un punct
    } else {
        int detAb = (d1.b*d2.c - d1.c*d2.b);
        if(detAb == 0) detAb = (d1.a*d2.c - d1.c*d2.a);

        if(detAb==2) return -1; /// multimea vida
    }

    return 1; ///dreptele coincid
}

bool pointOnSegment(Punct A, Punct B, Punct p) {
    if(A.x <= p.x && B.x >= p.x &&
       A.y <= p.y && B.y >= p.y)
        return true;

    if(A.x >= p.x && B.x <= p.x &&
       A.y >= p.y && B.y <= p.y)
        return true;

    return false;
}

bool uniqueSolution() {
    return true;
}

bool segmentsIntersection(Punct A, Punct B, Punct C, Punct D) {
    Punct st, dr;

    if(A.x < C.x)
}

int main()
{
    vector<Punct> puncte;

    freopen("data.in", "r", stdin);
    read(puncte);

    Dreapta d1 = computeSegment(puncte[0], puncte[1]);
    Dreapta d2 = computeSegment(puncte[2], puncte[3]);

    Punct p;
    int err = linesIntersection(d1, d2, p);

    if(err == 0) {
        if(pointOnSegment(puncte[0], puncte[1], p) && pointOnSegment(puncte[2], puncte[3], p))
            printf("Intersectia e un punct: (%.2f, %.2f)\n", p.x, p.y);
        else
            printf("Multimea vida!");
    } else if(err == 1) {


    }
}
