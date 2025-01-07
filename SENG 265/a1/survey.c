#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* get test type is givein the line that says what type of test are wanting to be preformed and puts in into an array */
void get_test_type ( char line[], char info[4] ) {
	int n = 0; 
	char *Ptr = strtok(line, ",");
	while ( Ptr != NULL ) {
		info[n] = *Ptr - 48; 
		n++;
		Ptr = strtok(NULL, ",");
	}
}


void print_into ( int size ) { // Prints the into for the output and number of responses 
	printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\nSURVEY RESPONSE STATISTICS\n\nNUMBER OF RESPONDENTS: %d\n\n", size);
}

void print_questions ( char Q[], int n ) { // is given a question and puts in into stdout
	printf("%s\n", Q);
}

void print_answers ( char Ans[], double val ) { // is given an of the the answers with the persentage it was picked and prints it
	printf("%.2f: %s\n", val, Ans);
}

void print_Q_title () { // Prints title when the questions are wanted 
	printf("FOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT\n\n");
}

void what_score ( double* a, int v, int i ) { // determins if the score of the question is Direst (0) or Reverse (1) and then adds the corisponding value to the given double pointer
	if( i == 0 ) {
		if( v == 0 ) {
			*a = *a + 1;
		}
		if( v == 1 ) {
			*a = *a + 2;
		}
		if( v == 2 ) {
			*a = *a + 3;
		} 
		if( v == 3 ) {
			*a = *a + 4;
		} 
		if( v == 4 ) {
			*a = *a + 5;
		}
		if( v == 5 ) {
			*a = *a + 6;
		}
	}
	if( i == 1 ) {
		if( v == 0 ) {
			*a = *a + 6;
		}
		if( v == 1 ) {
			*a = *a + 5;
		}
		if( v == 2 ) { 
			*a = *a + 4;
		}
		if( v == 3 ) {
			*a = *a + 3;
		}
		if( v == 4 ) {
			*a = *a + 2;
		}
		if( v == 5 ) {
			*a = *a + 1;
		}
	}
}

void what_ans ( double* a, double* b, double* c, double* d, double* e, double* f, int v ) { // determins what the answer is and adds 20% to that answer pointer 
	if( v == 0 ) {
		*a = *a + 20; 
	} 
	if( v == 1 ) {
		*b = *b + 20;
	} 
	if( v == 2 ) {
		*c = *c + 20;
	} 
	if( v == 3 ) {
		*d = *d + 20;
	} 
	if( v == 4 ) {
		*e = *e + 20;
	} 
	if( v == 5 ) {
		*f = *f + 20;
	}
}

void print_3_title () { // Prints the title if scores are wanted 
	printf("SCORES FOR ALL THE RESPONDENTS\n\n");
}

void print_4_title () { // Prints the title is the average score is wanted 
	printf("AVERAGE SCORES PER RESPONDENT\n\n");
}

void print_scores ( double a[], double b[], double d[], double e[], double f[] ) { // Prints the scores given it it 
	double c = *a;
	double i = *b;
	double g = *d;
	double u = *e;
	double p = *f;
	printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n", c, i, g, u, p);
}

void get_average ( double* a, double* b, double* c, double* d, double* e, double i ) { // takes the each score and divides it by the number if respnses and buts the average back into the score pointer 
	*a = *a / i;
	*b = *b / i;
	*c = *c / i;
	*d = *d / i;
	*e = *e / i;
}

void get_score ( char G[], char W[], double* ptr, int v, int i ) { // takes the answer given (G), the answer we are looking for (W), a pointer to the value of the catigory (ptr), what answer we are looking for number value (v), and if the answer is Direst or Reverse (i)
	if( strcmp(G, W) == 0 ) { // checks if the responce matches the answer type that is being checked 
		what_score(ptr, v, i);
	}
}

void get_average_score (double f[], double g[], double h[], double i[], double j[], double* ptr, int num ) { // takes the scores for the five people answering and finds the average score in each catigoty
	double a = *f;
	double b = *g;
	double c = *h;
	double d = *i;
	double e = *j;
	*ptr = (a + b + c + d + e) / num;
}


int main (int argc, char *argv[]) {

	int n = 0;

	char test_line1[100];
	char test_line2[80];
	char test_line3[250];
	char test_line4[70];

	fgets( test_line1, 100, stdin ); // Gets the first four lines that is not important information 
	fgets( test_line2, 80, stdin );
	fgets( test_line3, 250, stdin );
	fgets( test_line4, 70, stdin );

	char test_type[4]; // Gets the line that tells you what types of information need to be displayed 
	char line1[10];
	fgets( line1, 10, stdin);
	get_test_type(line1,test_type);

	char test_line5[60]; // Get line with no inportant information 
	fgets( test_line5, 60, stdin );

	char Qs[38][110]; // Makes an Array of Strings out of the line of questions asked
	char line2[3000];
	fgets( line2, 3000, stdin );
	char *Ptr = strtok(line2, ";");
	while ( Ptr != NULL ) {
		strcpy(Qs[n], Ptr);
		n++;
		Ptr = strtok(NULL, ";");
	}
	Ptr = strtok(Qs[37], "\n"); // The last question has a \n at the end of it and not ; so when comparing and printing this \n will mess up the formating and if you can compare them accurately
	strcpy(Qs[37], Ptr);

	n = 0;

	char test_line6[130]; // Gets line of instructions out of the way 
	fgets( test_line6, 130, stdin );

	char Odr[38][8]; // Makes a Array of String for the order in witch the question responces will be scored 
	char line3[300];
	fgets( line3, 300, stdin );
	Ptr = strtok(line3, ";");
	while ( Ptr != NULL ) {
		strcpy(Odr[n], Ptr);
		n++;
		Ptr = strtok(NULL, ";");
	}
	Ptr = strtok(Odr[37], "\n"); // Removing the \n from the last String in the array
	strcpy(Odr[37], Ptr);

	n = 0;

	char test_line7[50]; // Gets line of instructions out of the way
	fgets( test_line7, 50, stdin );	

	char Ans[6][20]; // Makes a Array of Strings containing the Answer that can be solected 
	char line4[100];
	fgets( line4, 100, stdin );
	Ptr = strtok(line4, ",");
	while ( Ptr != NULL ) {
		strcpy(Ans[n], Ptr);
		n++;
		Ptr = strtok(NULL, ",");
	}
	Ptr = strtok(Ans[5], "\n"); // Removing the \n from the last String in the Array
	strcpy(Ans[5], Ptr);

	if( test_type[0] == 1 ) { // If there are no responces and the formating for the questions needs to be checked 
		print_into(0);
		print_Q_title();
		n = 0;
		double h = 0.00;
		while ( n < 38 ) {
			print_questions(Qs[n], n);
			int j = 0;
			while ( j < 6 ) {
				print_answers(Ans[j], h);
				j++;
			}
			if( n < 37 ) {
				printf("\n");
			}
			n++;
		}
		return(-1); // Because there are no responces there is no need to continue so this stops the program 
	}

	char test_line8[45]; // Gets instructon out of the way 
	fgets( test_line8, 45, stdin );

	char Ans1[41][20];
	char Ans2[41][20];
	char Ans3[41][20];
	char Ans4[41][20];
	char Ans5[41][20];

	char Ans_line1[750];
	char Ans_line2[750];
	char Ans_line3[750];
	char Ans_line4[750];
	char Ans_line5[750];

	n = 0;
	fgets( Ans_line1, 750, stdin ); // Makes an Array of Strings with the responces 
	Ptr = strtok(Ans_line1, ",");
	while ( Ptr != NULL ) {
		strcpy(Ans1[n], Ptr);
		n++;
		Ptr = strtok(NULL, ",");
	}
	Ptr = strtok(Ans1[40], "\n");
	strcpy(Ans1[40], Ptr);

	n = 0;
	fgets( Ans_line2, 750, stdin );
	Ptr = strtok(Ans_line2, ",");
	while ( Ptr != NULL ) {
		strcpy(Ans2[n], Ptr);
		n++;
		Ptr = strtok(NULL, ",");
	}
	Ptr = strtok(Ans2[40], "\n");
	strcpy(Ans2[40], Ptr);

	n = 0;
	fgets( Ans_line3, 750, stdin );
	Ptr = strtok(Ans_line3, ",");
	while ( Ptr != NULL ) {
		strcpy(Ans3[n], Ptr);
		n++;
		Ptr = strtok(NULL, ",");
	}
	Ptr = strtok(Ans3[40], "\n");
	strcpy(Ans3[40], Ptr);

	n = 0;
	fgets( Ans_line4, 750, stdin );
	Ptr = strtok(Ans_line4, ",");
	while ( Ptr != NULL ) {
		strcpy(Ans4[n], Ptr);
		n++;
		Ptr = strtok(NULL, ",");
	}
	Ptr = strtok(Ans4[40], "\n");
	strcpy(Ans4[40], Ptr);

	n = 0;
	fgets( Ans_line5, 750, stdin );
	Ptr = strtok(Ans_line5, ",");
	while ( Ptr != NULL ) {
		strcpy(Ans5[n], Ptr);
		n++;
		Ptr = strtok(NULL, ",");
	}
	Ptr = strtok(Ans5[40], "\n");
	strcpy(Ans5[40], Ptr); 
	
	n = 0;

	print_into(5);

	if( test_type[1] == 1 ) { // When the percentage for the answers for each questons wants to be procesed
		double A = 0.00;
		double B = 0.00;
		double C = 0.00;
		double D = 0.00;
		double E = 0.00;
		double F = 0.00;

		double* a = &A;
		double* b = &B;
		double* c = &C;
		double* d = &D;
		double* e = &E;
		double* f = &F;

		print_Q_title();

		int j = 3;
		int v = 0;

		while ( n < 38 ) { // Gose through each question to compile the responces to each question 
			A = 0;
			B = 0;
			C = 0;
			D = 0;
			E = 0;
			F = 0;
			v = 0;
			while ( v < 6 ) {
				if( strcmp(Ans1[j], Ans[v]) == 0 ) { // Finds what responce was given 
					what_ans(a, b, c, d, e, f, v);
				}
				v++;
			}
			v = 0;

			while ( v < 6 ) {
				if( strcmp(Ans2[j], Ans[v]) == 0 ) {
					what_ans(a, b, c, d, e, f, v);
				}
				v++;
			}
			v = 0;

			while ( v < 6 ) {
				if( strcmp(Ans3[j], Ans[v]) == 0 ) {
					what_ans(a, b, c, d, e, f, v);
				}
				v++;
			}
			v = 0;

			while ( v < 6 ) {
				if( strcmp(Ans4[j], Ans[v]) == 0 ) {
					what_ans(a, b, c, d, e, f, v);
				}
				v++;
			}
			v = 0; 

			while ( v < 6 ) {
				if( strcmp(Ans5[j], Ans[v]) == 0 ) {
					what_ans(a, b, c, d, e, f, v);
				}
				v++;
			}
			v = 0; 
			
			print_questions(Qs[n], n); 
			print_answers(Ans[0], A); // Prints out each responce before going on to the next question 
			print_answers(Ans[1], B);
			print_answers(Ans[2], C);
			print_answers(Ans[3], D);
			print_answers(Ans[4], E);
			print_answers(Ans[5], F);
			if( n < 37 ) {		
				printf("\n"); // Dose not need \n for the last question 
			}

			j++;
			n++;
		}
	}
	
	/* Makes five Array and five pointers so the scores can be found and stored */
	double person1[5] = {0.00, 0.00, 0.00, 0.00, 0.00};
	double person2[5] = {0.00, 0.00, 0.00, 0.00, 0.00};
	double person3[5] = {0.00, 0.00, 0.00, 0.00, 0.00};
	double person4[5] = {0.00, 0.00, 0.00, 0.00, 0.00};
	double person5[5] = {0.00, 0.00, 0.00, 0.00, 0.00};

	double *a = &person1[0];
	double *b = &person2[0];
	double *c = &person3[0];
	double *d = &person4[0];
	double *e = &person5[0];

	n = 0;
		
	char str1[] = "Direct";
	char str2[] = "Reverse";

	int j = 3;
	int v = 0;

	while ( n < 8 ) {
		if( strcmp(Odr[n], str1) == 0 ) { // sorts out if responces are direct or reverse 
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 0); 
				get_score(Ans2[j], Ans[v], b, v, 0);
				get_score(Ans3[j], Ans[v], c, v, 0);
				get_score(Ans4[j], Ans[v], d, v, 0);
				get_score(Ans5[j], Ans[v], e, v, 0);
				v++;
			}
			v = 0; 
		
		}
		if( strcmp(Odr[n], str2) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 1);
				get_score(Ans2[j], Ans[v], b, v, 1);
				get_score(Ans3[j], Ans[v], c, v, 1);
				get_score(Ans4[j], Ans[v], d, v, 1);
				get_score(Ans5[j], Ans[v], e, v, 1);
				v++;
			}
			v = 0;
		}
		j++;
		n++;
	}
	
	get_average(a, b, c, d, e, 8);

	a = &person1[1]; // changes pointers to next spot in score arrays for each person
	b = &person2[1];
	c = &person3[1];
	d = &person4[1];
	e = &person5[1];
	while ( n < 18 ) {
		if( strcmp(Odr[n], str1) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 0);
				get_score(Ans2[j], Ans[v], b, v, 0);
				get_score(Ans3[j], Ans[v], c, v, 0);
				get_score(Ans4[j], Ans[v], d, v, 0);
				get_score(Ans5[j], Ans[v], e, v, 0);
				v++;
			}
			v = 0;
		}
		if( strcmp(Odr[n], str2) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 1);
				get_score(Ans2[j], Ans[v], b, v, 1);
				get_score(Ans3[j], Ans[v], c, v, 1);
				get_score(Ans4[j], Ans[v], d, v, 1);
				get_score(Ans5[j], Ans[v], e, v, 1);
				v++;
			}
			v = 0;
		}
		j++; 
		n++;
	}

	get_average(a, b, c, d, e, 10);

	a = &person1[2];
	b = &person2[2];
	c = &person3[2];
	d = &person4[2];
	e = &person5[2];
	while ( n < 28 ) {
		if( strcmp(Odr[n], str1) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 0);
				get_score(Ans2[j], Ans[v], b, v, 0);
				get_score(Ans3[j], Ans[v], c, v, 0);
				get_score(Ans4[j], Ans[v], d, v, 0);
				get_score(Ans5[j], Ans[v], e, v, 0);
				v++;
			}
			v = 0;
		}
		if( strcmp(Odr[n], str2) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 1);
				get_score(Ans2[j], Ans[v], b, v, 1);
				get_score(Ans3[j], Ans[v], c, v, 1);
				get_score(Ans4[j], Ans[v], d, v, 1);
				get_score(Ans5[j], Ans[v], e, v, 1);
				v++;
			}
			v = 0;
		}
		j++;
		n++;
	}

	get_average(a, b, c, d, e, 10);

	a = &person1[3];
	b = &person2[3];
	c = &person3[3];
	d = &person4[3];
	e = &person5[3];
	while ( n < 34 ) {
		if( strcmp(Odr[n], str1) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 0);
				get_score(Ans2[j], Ans[v], b, v, 0);
				get_score(Ans3[j], Ans[v], c, v, 0);
				get_score(Ans4[j], Ans[v], d, v, 0);
				get_score(Ans5[j], Ans[v], e, v, 0);
				v++;
			}
			v = 0;
		}
		if( strcmp(Odr[n], str2) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 1);
				get_score(Ans2[j], Ans[v], b, v, 1);
				get_score(Ans3[j], Ans[v], c, v, 1);
				get_score(Ans4[j], Ans[v], d, v, 1);
				get_score(Ans5[j], Ans[v], e, v, 1);
				v++;
			}
			v = 0;
		}
		j++;
		n++;
	}

	get_average(a, b, c, d, e, 6);

	a = &person1[4];
	b = &person2[4];
	c = &person3[4];
	d = &person4[4];
	e = &person5[4];
	while ( n < 38 ) {
		if( strcmp(Odr[n], str1) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 0);	
				get_score(Ans2[j], Ans[v], b, v, 0);
				get_score(Ans3[j], Ans[v], c, v, 0);
				get_score(Ans4[j], Ans[v], d, v, 0);
				get_score(Ans5[j], Ans[v], e, v, 0);
				v++;
			}
			v = 0;
		}
		if( strcmp(Odr[n], str2) == 0 ) {
			while ( v < 6 ) {
				get_score(Ans1[j], Ans[v], a, v, 1);
				get_score(Ans2[j], Ans[v], b, v, 1);
				get_score(Ans3[j], Ans[v], c, v, 1);
				get_score(Ans4[j], Ans[v], d, v, 1);
				get_score(Ans5[j], Ans[v], e, v, 1);
				v++;
			}
			v = 0;
		}
		j++;
		n++;
	}

	get_average(a, b, c, d, e, 4);

	if( test_type[2] == 1 ) { // Prints out the componets for the scores for each person how responded 
		if( test_type[1] == 1 ) { // Prints out extra blank line for formating 
			printf("\n");
		}
		print_3_title();

		a = &person1[0]; b = &person1[1]; c = &person1[2]; d = &person1[3]; e = &person1[4];
		print_scores(a, b, c, d, e);
		
		a = &person2[0]; b = &person2[1]; c = &person2[2]; d = &person2[3]; e = &person2[4];
		print_scores(a, b, c, d, e);

		a = &person3[0]; b = &person3[1]; c = &person3[2]; d = &person3[3]; e = &person3[4];
		print_scores(a, b, c, d, e);

		a = &person4[0]; b = &person4[1]; c = &person4[2]; d = &person4[3]; e = &person4[4];
		print_scores(a, b, c, d, e);

		a = &person5[0]; b = &person5[1]; c = &person5[2]; d = &person5[3]; e = &person5[4];
		print_scores(a, b, c, d, e);
	}

	double Avg[5] = {0.00, 0.00, 0.00, 0.00, 0.00};

	double *avg_ptr = &Avg[0];

	if( test_type[3] == 1 ) { // Prints out points average for all the responces 
		if( test_type[2] == 1 || test_type[3] == 1 ) { // Prints out extra line to get fomating right 
			printf("\n");
		}
		print_4_title();

		a = &person1[0]; b = &person2[0]; c = &person3[0]; d = &person4[0]; e = &person5[0];
		get_average_score(a, b, c, d, e, avg_ptr, 5);
		
		avg_ptr = &Avg[1]; // moves pointer to next node in Average Score Array

		a = &person1[1]; b = &person2[1]; c = &person3[1]; d = &person4[1]; e = &person5[1];
		get_average_score(a, b, c, d, e, avg_ptr, 5);
		
		avg_ptr = &Avg[2];

		a = &person1[2]; b = &person2[2]; c = &person3[2]; d = &person4[2]; e = &person5[2];
		get_average_score(a, b, c, d, e, avg_ptr, 5);
		
		avg_ptr = &Avg[3];

		a = &person1[3]; b = &person2[3]; c = &person3[3]; d = &person4[3]; e = &person5[3];
		get_average_score(a, b, c, d, e, avg_ptr, 5);
		
		avg_ptr = &Avg[4];

		a = &person1[4]; b = &person2[4]; c = &person3[4]; d = &person4[4]; e = &person5[4];
		get_average_score(a, b, c, d, e, avg_ptr, 5);

		a = &Avg[0]; b = &Avg[1]; c = &Avg[2]; d = &Avg[3]; e = &Avg[4];
		print_scores(a, b, c, d, e);
	}

	return 0;
}
