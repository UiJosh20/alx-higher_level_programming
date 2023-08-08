#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: head of the node
 * @number: the number to be added
 * Return: the address of the new node or NULL if it failed
 */
lisint_t *insert_node(listint_t **head, int number)
{
	listint_t *loader;
	lisint_t *new;

	loader = *head;
	new - malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (loader->next != NULL)
	{
		if ((loader->next)->n >= number)
		{
			new->next = loader->next;
			loader->next = new;
			return (new);
		}
		loader = loader->next;
	}
	new->next = NULL;
	loader->next = new;
	return (new);
}
