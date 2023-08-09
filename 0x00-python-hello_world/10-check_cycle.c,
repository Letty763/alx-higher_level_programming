#include "lists.h"

/**
 * check_cycle - Evaluates whether a linked list contains a cycle.
 * @list: This will be the linked list that requires inspection for cycles. *
 * Return: Return 1 if the list contains a cycle, and 0 if it does not. */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
