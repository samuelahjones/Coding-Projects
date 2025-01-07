#ifndef _INPUT_HANDLING_H_
#define _INPUT_HANDLING_H_

#include "dyn_survey.h"

int tokenize_line( char *line, char **phrases, char delimiter[]);

int process_tests( char **phrases, int num_phrases, short *tests);

void process_question_types( char **phrases, int num_phrases, short *question_types );

void process_response( char **phrases, int num_phrases, short *question_types, Respondent *responses, int num );

double convert_response_to_scale(char *token );

double reverce_scale( double scale );

int get_num_responses( char **phrases );

int count_tokens( char *line, char delimiter[] );

void get_conditions( char **phrases, int num_phrases, int conditions[], int num );

void turn_on( Respondent *responses, int num_responses );


#endif
