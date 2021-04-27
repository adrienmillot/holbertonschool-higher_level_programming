#include "lists.h"
#include <stdlib.h>

/**
 * createNode - create a new node
 *
 * @prmNbr: number
 *
 * Return: new element
 */
listint_t *createNode(const int prmNbr)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = prmNbr;

	return (new);
}

/**
 * add_nodeint - adds a new node at the beginning of a list_t list
 *
 * @head: pointer to last element
 * @n: number
 *
 * Return: new last element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);

	new = createNode(number);
	if (new == NULL)
		return (NULL);

	if (*head == NULL)
		*head = new;
	else
	{
		new->next = *head;
		*head = new;
	}

	return (new);
}
