#include "input_handling.h"
#include "emalloc.h"

int tokenize_line( char *line, char **phrases, char delimiter[] ) {

	int num_phrases = 0;
	char *token;

	token = strtok(line, delimiter);

	while ( token ) {
		phrases[num_phrases] = (char *)emalloc(sizeof(char) * (strlen(token)+1));
		strncpy(phrases[num_phrases], token, strlen(token)+1);
		num_phrases++;

		token = strtok(NULL, delimiter);
	}
	return num_phrases;
}


int process_tests( char **phrases, int num_phrases, short *tests ) {
	for ( int i = 0; i < num_phrases; i++ ) {
	       if( phrases[i][0] == '1' ) {
	      		tests[i] = 1;
	       }
	       else {
			tests[i] = 0;
	       }
	}
	return num_phrases;
}
		

void process_question_types( char **phrases, int num_phrases, short *question_types ) {
	for ( int i = 0; i < num_phrases; i++ ) {
		if( strcmp(phrases[i], "Direct" ) == 0 ) {
			question_types[i] = 1;
		}
		else {
			question_types[i] = 0;
		}
	}
	return;
}


void process_response( char **phrases, int num_phrases, short *question_types, Respondent *responses, int num ) {
	for( int i = 0; i < num_phrases; i++ ) {
		if( i == 0 ) {
			int j = strlen(phrases[i]) + 1;
			responses[num].name = (char *)emalloc(sizeof(char) * j);
			strncpy(responses[num].name, phrases[i], j);
		}
		else if( i == 2 ) {
			char line[4];
			strncpy(line, phrases[i], 4);
			int year = atoi(line);
			year = 2024 - year;
			responses[num].age = year;
		}
		else if( i == 1 ) {
			if( strcmp(phrases[i], "yes") == 0 ) {
				responses[num].canadian = 1;
			}
			else {
				responses[num].canadian = 0;
			}
		}
		else {
			double scale = convert_response_to_scale(phrases[i]);
			responses[num].responses[i-3].ans = scale;
			if( question_types[i-3] == 0 ) {
				responses[num].responses[i-3].wight = reverce_scale(scale);
			}
			else {
				responses[num].responses[i-3].wight = scale;
			}
		}
	}		
	return;
}	


double convert_response_to_scale( char *token ) {
	double scale;
	if( strcmp(token, "fully disagree") == 0 ) {
		scale = 1;
	}
	else if( strcmp(token, "disagree") == 0 ) {
		scale = 2;
	}
	else if( strcmp(token, "partially disagree") == 0 ) {
		scale = 3;
	} 
	else if( strcmp(token, "partially agree") == 0 ) {
		scale = 4;
	}
	else if( strcmp(token, "agree") == 0 ) {
		scale = 5;
	}
	else {
		scale = 6;
	}

	return scale;
}


double reverce_scale( double scale ) {
	double rev;
	if( scale == 1 ) {
		rev = 6;
	}
	else if( scale == 2 ) {
		rev = 5;
	}
	else if( scale == 3 ) {
		rev = 4;
	}
	else if( scale == 4 ) {
		rev = 3;
	}
	else if( scale == 5 ) {
		rev = 2;
	}
	else {
		rev = 1;
	}
	return rev;
}


int get_num_responses( char **phrases ) {
	int res = 0;
	
	if( phrases[0][0] == '2' ) {
		res = 2;
	}
	else if( phrases[0][0] == '4' ) {
		res = 4;
	}
	else if( phrases[0][0] == '5' ) {
		res = 5;
	}
	else {
		res = 10;
	}
	return res;
}


int count_tokens( char *line, char delimiter[] ) {
	int num_tokens = 0;
	char *token;

	token = strtok(line, delimiter);

	while(token) {
		num_tokens++;

		token = strtok(NULL, delimiter);
	}
	return num_tokens;
}


void get_conditions( char **phrases, int num_phrases, int conditions[], int num ) {
	if( strcmp(phrases[0], "0") == 0 ) {
		if( strcmp(phrases[1], "Engineering") == 0 ) {
			conditions[0] = 1;
			return;
		} else if( strcmp(phrases[1], "Health") == 0 ) {
			conditions[0] = 2;
			return;
		} else {
			conditions[0] = 3;
			return;
		}
	} else if( strcmp(phrases[0], "1") == 0 ) {
		if( strcmp(phrases[1], "yes") == 0 ) {
			conditions[1] = 1;
			return;
		} else {
			conditions[1] = 2;
			return;
		}
	} else {
		int a = atoi(phrases[1]);
		int b = atoi(phrases[2]);
		conditions[2] = a;
		conditions[3] = b;
		return;
	}
}

void turn_on( Respondent *responses, int num_responses ) {
	for( int i = 0; i < num_responses; i++ ) {
		responses[i].on_or_off = 1;
	}
}
