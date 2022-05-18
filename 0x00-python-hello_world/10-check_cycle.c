#include "lists.h"
/**
 *check_cycle - Check a circule list
 *@list: header of the list
 *Return: 1 or 0 if is or isn't a cicrcule list
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	list->n = -999;
	list = list->next;
	while (list != NULL)
	{
		if (list->n == -999)
			return (1);
		list->n = -999;
		list = list->next;
	}
	return (0);
}
