#include "dyn_survey.h"
#include "input_handling.h"
#include "processing.h"
#include "output.h"
#include "emalloc.h"

int main (int argc, char *argv[]) {

	if( argc != 1 ) {
		printf("Usage: %s\n", argv[0]);
		printf("Reads from stdin and should not receive parameters\n");
		exit(1);
	}

	/* Declaration and initialization of local variables */
	int num_phrases = 0;
	char **phrases;

	int num_tests = 0;
	short *tests;

	int num_questions = 0; 
	char **questions;
	short *question_types;

	int num_likert_levels = 0;
	char **likert_level_descriptions;
	
	int num_respondents = 0;
	Respondent *responses;

	double frequencies[NUMBER_QUESTIONS][NUMBER_RESPONSES];
	for( int i = 0; i < NUMBER_QUESTIONS; i++ ) {
		for( int j = 0; j < NUMBER_RESPONSES; j++ ) {
			frequencies[i][j] = 0.0;
		}
	}

	double average_scores[NUMBER_SCORES];

	int conditions[4] = {0, 0, 0, 0};

	char *line = (char *)emalloc(sizeof(char) * MAX_LINE_LENGTH);
	char *line_copy = (char *)emalloc(sizeof(char) * MAX_LINE_LENGTH);

	int n = 0;
	int g = 0;

	int phase = 0;
	
	/* Reads input lines and proscess them */
	while( fgets(line, sizeof(char) * MAX_LINE_LENGTH, stdin) ) {
		if( line[0] == '#' ) {
			continue;
		}
		strncpy(line_copy, line, strlen(line)+1);
		switch (phase) {
		case 0:
			num_phrases = count_tokens(line_copy, ",\n");
			phrases = (char **)emalloc(sizeof(char *) * num_phrases);
			tokenize_line(line, phrases, ",\n");
			tests = (short *)emalloc(sizeof(short) * num_phrases);
			num_tests = process_tests(phrases, num_phrases, tests);
			phase++;
			for( int i = 0; i < num_phrases; i++ ) {
				free(phrases[i]);
			}
			free(phrases);
			break;
		case 1:
			num_questions = count_tokens(line_copy, ";\n");
			questions = (char **)emalloc(sizeof(char *) * num_questions);
			tokenize_line(line, questions, ";\n");
			phase++;
			break;
		case 2:
			num_phrases = count_tokens(line_copy, ";\n");
			phrases = (char **)emalloc(sizeof(char *) * num_phrases);
			tokenize_line(line, phrases, ";\n");
			question_types = (short *)emalloc(sizeof(short) * num_phrases);
			process_question_types(phrases, num_phrases, question_types);
			phase++;
			for(int i = 0; i < num_phrases; i++ ) {
				free(phrases[i]);
			}
			free(phrases);
			break;
		case 3:
			num_likert_levels = count_tokens(line_copy, ",\n");
			likert_level_descriptions = (char **)emalloc(sizeof(char *) * num_likert_levels);
			tokenize_line(line, likert_level_descriptions, ",\n");
			phase++;
			break;
		case 4:
			num_phrases = count_tokens(line_copy, "\n");
			phrases = (char **)emalloc(sizeof(char *) * num_phrases);
			tokenize_line(line, phrases, "\n");
			num_respondents = get_num_responses(phrases);
			responses = (Respondent *)emalloc(sizeof(Respondent) * num_respondents);
			turn_on(responses, num_respondents);
			phase++;
			for( int i = 0; i < num_phrases; i++ ) {
				free(phrases[i]);
			}
			free(phrases);
			break;
		case 5:
			num_phrases = count_tokens(line_copy, ",\n");
			if( n == 0 ) {
				phrases = (char **)emalloc(sizeof(char *) * num_phrases);
			}
			tokenize_line(line, phrases, ",\n");
			process_response(phrases, num_phrases, question_types, responses, n);
			n++;
			if( n == num_respondents ) {
				phase++;
				for( int i = 0; i < num_phrases; i++ ) {
					free(phrases[i]);
				}
				free(phrases);
			}
			break;
		case 6:
			num_phrases = count_tokens(line_copy, ",\n");
			phrases = (char **)emalloc(sizeof(char *) * num_phrases);
			tokenize_line(line, phrases, ",\n");
			get_conditions(phrases, num_phrases, conditions, g);
			g++;
			for( int i = 0; i < num_phrases; i++ ) {
				free(phrases[i]);
			}
			free(phrases);
			break;
		}
	}
	

	double scores[num_respondents][NUMBER_SCORES];
	for( int i = 0; i < num_respondents; i++ ) {
        	for( int j = 0; j < NUMBER_SCORES; j++ ) {
            		scores[i][j] = 0.0;
       		}
    	}

	/* survey data procesed and stored for output */

	compute_conditions_one(conditions, responses, num_respondents);

	compute_conditions_two(conditions, responses, num_respondents);

	compute_conditions_three(conditions, responses, num_respondents);

	compute_frequencies(frequencies, num_questions, responses, num_respondents, num_likert_levels);

	compute_scores(scores, responses, num_respondents);

	int used = responses_used(responses, num_respondents);

	compute_average_scores(average_scores, scores, used, num_respondents);

	/* Prints results */
	print_output(tests, num_tests, questions, num_questions, likert_level_descriptions, num_likert_levels, responses, num_respondents,
			frequencies, scores, average_scores, used);

	/* frees memory */
	for( int i = 0; i < num_respondents; i++ ) {
		free(responses[i].name);
	}

	free(responses);
	free(line);
	free(line_copy);
	free(question_types);
	free(tests);

	for( int i = 0; i < num_questions; i++ ) {
		free(questions[i]);
	}

	for( int i = 0; i < num_likert_levels; i++ ) {
		free(likert_level_descriptions[i]);
	}

	return 0;
}
