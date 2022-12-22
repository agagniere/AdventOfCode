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
	int    data;
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
	int     move = node->data % (size - 1);

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

char* _itoa(const int* i)
{
	return ft_itoa(*i);
}

int main()
{
	t_array encrypted[] = {NEW_ARRAY(Node*)};
	t_array decrypted[] = {NEW_ARRAY(int)};
	t_list  mixed[1];

	ftl_init(mixed, sizeof(Node));

	{
		char*   line        = NULL;
		while (get_next_line(STDIN_FILENO, &line) == 1)
		{
			ftl_push_back(mixed, (t_node*)(Node[]){{.data = ft_atoi(line)}});
			fta_append(encrypted, &mixed->root.prev, 1);
			free(line);
			line = NULL;
		}
	}

	ft_printf("%zu == %zu\n", encrypted->size, mixed->size);
	fta_iter2(encrypted, exec_one, &mixed->size, mixed);

	{
		t_node* zero = mixed->root.next;
		while (((Node*)zero)->data)
			zero = zero->next;
		fta_append(decrypted, &((Node*)zero)->data, 1);
		t_node* ptr = zero->next;
		while (ptr != zero)
		{
			if (ptr != (t_node*)mixed)
				fta_append(decrypted, &((Node*)ptr)->data, 1);
			ptr = ptr->next;
		}
	}

	ft_printf("%s\n", fta_string(decrypted, (char* (*)(void*))_itoa));
	int x = ARRAY_GETL(int, decrypted, 1000 % (decrypted->size));
	int y = ARRAY_GETL(int, decrypted, 2000 % (decrypted->size));
	int z = ARRAY_GETL(int, decrypted, 3000 % (decrypted->size));
	ft_printf("%i, %i, %i\n", x, y, z);
	ft_printf("%i\n", x + y + z);
	return 0;
}
