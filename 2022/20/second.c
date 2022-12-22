#include <ft_array.h>
#include <ft_deque.h>
#include <ft_list.h>
#include <ft_prepro/tools.h>
#include <ft_printf.h>
#include <get_next_line.h>
#include <libft.h>

#include <unistd.h>
#include <stdlib.h>

typedef struct
{
	t_node super;
	long    data;
} Node;

static inline void detach(t_node* self)
{
	self->prev->next = self->next;
	self->next->prev = self->prev;
}

static inline void insert_after(t_node* self, t_node* node)
{
	self->prev = node;
	self->next = node->next;
	node->next->prev = self;
	node->next = self;
}

void exec_one(const size_t* length, const t_list* list, Node** self)
{
	Node*   node = *self;
	t_node* ptr  = (t_node*)node;
	int     size = *length;
	long    move = node->data % (size - 1);

	if (move < -size / 2)
		move += size - 1;
	else if (move > size / 2)
		move -= size - 1;
	if (!move)
		return ;
	detach((t_node*)node);
	if (move > 0)
	{
		while (ptr == (t_node*)list || move --> 0)
			ptr = ptr->next;
		insert_after((t_node*)node, ptr);
	}
	else
	{
		while (ptr == (t_node*)list || move++ < 0)
			ptr = ptr->prev;
		insert_after((t_node*)node, ptr->prev);
	}
}

char* _itoa(const long* i)
{
	return ft_itoa(*i);
}

static const long key = 811589153;

int main()
{
	t_array encrypted[] = {NEW_ARRAY(Node*)};
	t_array decrypted[] = {NEW_ARRAY(long)};
	t_list  mixed[1];

	ftl_init(mixed, sizeof(Node));

	{
		char*   line        = NULL;
		while (get_next_line(STDIN_FILENO, &line) == 1)
		{
			ftl_push_back(mixed, (t_node*)(Node[]){{.data = key * ft_atoi(line)}});
			fta_append(encrypted, &mixed->root.prev, 1);
			free(line);
			line = NULL;
		}
	}


	ft_printf("%zu == %zu\n", encrypted->size, mixed->size);
	for (int _ = 0; _ < 10; _++)
		fta_iter2(encrypted, exec_one, &mixed->size, mixed);

	{
		Node* zero = (Node*)mixed->root.next;
		while (zero->data)
			zero = (Node*)zero->super.next;
		fta_append(decrypted, &zero->data, 1);
		Node* ptr = (Node*)zero->super.next;
		while (ptr != zero)
		{
			if (ptr != (void*)&mixed)
				fta_append(decrypted, &ptr->data, 1);
			ptr = (Node*)ptr->super.next;
		}
	}

	ft_printf("%s\n", fta_string(decrypted, (char* (*)(void*))_itoa));
	long x = ARRAY_GETL(long, decrypted, 1000 % (decrypted->size));
	long y = ARRAY_GETL(long, decrypted, 2000 % (decrypted->size));
	long z = ARRAY_GETL(long, decrypted, 3000 % (decrypted->size));
	ft_printf("%li, %li, %li\n", x, y, z);
	ft_printf("%li\n", x + y + z);
	return 0;
}
