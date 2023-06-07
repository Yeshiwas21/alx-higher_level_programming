#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * insert_node- Inserts a number into a sorted singly linked list.
 * @head: Head pointer
 * @number: integer
 * Return: nth node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_node, *actual_node = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t)); /* allocate node */
	if (new_node == NULL)
		return (NULL);

	new_node->n = number; /* put in the data  */
	new_node->next = NULL;

	if (actual_node == NULL || actual_node->n > number) /* no head and at beginning */
	{	new_node->next = actual_node;
		*head = new_node;
		return (new_node);
	}

	while (actual_node && number > actuactual_nodeal->n) /* Traverse till pos or last node */
	{	prev_node = actual_node;
		actual_node = actual_node->next;
	}

	prev_node->next = new_node; /* Change the next of prev node */
	new_node->next = actual_node;  /* point new to after */
	return (new_node);
}
