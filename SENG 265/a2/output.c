#include "output.h"

void print_output( short *test, int num_tests,
		char **questions, int num_questions,
		char **likert_level, int num_likert_levels,
		Respondent *responses, int num_respondents,
		double frequencies[][NUMBER_RESPONSES], double scores[][NUMBER_SCORES],
		double average_scores[], int used ) {

	/* prints header */
	printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    	printf("SURVEY RESPONSE STATISTICS\n");
    	printf("\nNUMBER OF RESPONDENTS: %d\n", used);

	if( test[0] == 1 ) {
        	printf("\nFOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT\n");

        	for (int i = 0; i < num_questions; i++) {
            		printf("\n%s\n", questions[i]);
            		for (int j = 0; j < num_likert_levels; j++) {
                		printf("%.2f: %s\n", frequencies[i][j], likert_level[j]);
            		}
        	}
    	}

    /* show respondents' scores */
    	if ( test[1] == 1 ) {
        	printf("\nSCORES FOR ALL THE RESPONDENTS\n");
        	printf("\n");
        	for (int i = 0; i < num_respondents; i++) {
			if( responses[i].on_or_off == 1 ) {
            			printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n", scores[i][0], scores[i][1], scores[i][2], scores[i][3], scores[i][4]);
			}
		}
    	}

    /* show average scores per respondent */
    	if ( test[2] == 1 ) {
        	printf("\nAVERAGE SCORES PER RESPONDENT\n");
        	printf("\n");
        	printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n", average_scores[0], average_scores[1], 
				average_scores[2], average_scores[3], average_scores[4]);
    	}

    	return;
}

