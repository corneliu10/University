#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#define NMAX 100

typedef struct coord {
	int row, col;
};

int mat1[NMAX][NMAX], mat2[NMAX][NMAX];
int n1, m1, n2, m2;

void *matrixCalc(void *arg) {
	struct coord *c = (struct coord*)arg;
	int *res = (int*)malloc(sizeof(int));
	*res = 0;

	for(int i=0; i<m1; i++)
		*res += mat1[c->row][i] * mat2[i][c->col];

	free(c);
	return res;
}

void printMatrix(int a[NMAX][NMAX], int n, int m) {
	for(int i=0; i<n; ++i) {
		for(int j=0; j<m; ++j)
			printf("%d ", a[i][j]);
		printf("\n");
	}
}

int main(int argc, char *argv[]) {
	if(argc != 1) {
		perror("Wrong number of args!");
		return errno;
	}

	freopen("data.in", "r", stdin);

	scanf("%d%d", &n1, &m1);
	for(int i=0; i<n1; ++i)
		for(int j=0; j<m1; ++j)
			scanf("%d", &mat1[i][j]);

	scanf("%d%d", &n2, &m2);
	for(int i=0; i<n2; ++i)
		for(int j=0; j<m2; ++j)
			scanf("%d", &mat2[i][j]);

	//printMatrix(mat1, n1, m1);
	//printMatrix(mat2, n2, m2);

	pthread_t tids[NMAX * NMAX];
	int nrThreads = 0;

	for(int i=0; i<n1; ++i)
		for(int j=0; j<m1; ++j, nrThreads++) 
		{
			struct coord *c = (struct coord*)malloc(sizeof(struct coord));
			c->row = i;
			c->col = j;
			if(pthread_create(&tids[nrThreads], NULL, matrixCalc, c)) {
				perror(NULL);
				return errno;
			}
		}

	void *res;
	int mat3[NMAX][NMAX];

	nrThreads = 0;
	for(int i=0; i<n1; ++i)
		for(int j=0; j<m1; ++j, nrThreads++) {
			if(pthread_join(tids[nrThreads], &res)) {
				perror(NULL);
				return errno;
			}

			mat3[i][j] = *(int *)res;
		}

	printMatrix(mat3, n1, m2);

	return 0;
}