#include "lists.h"

/**
 * reverse_listint - Reverses a singly linked list.
 * @head: Double pointer to the first node of the list.
 *
 * Return: Pointer to the reversed list.
 */
void reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the first node of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *first_half = *head;
    listint_t *second_half = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL)
        slow = slow->next;

    reverse_listint(&slow);
    second_half = slow;

    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
            return (0);

        first_half = first_half->next;
        second_half = second_half->next;
    }

    return (1);
}
