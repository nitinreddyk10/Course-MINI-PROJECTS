/*
In a vehicle showroom,we manufacture bikes and vehicles (we know manufacturing cost) and sell them to customers(we will get selling price) and calculate the net profit.(Assuming profits)
Using 2 linked lists we store information of bikes and vehicles seperately and their details. 

We will:
1.Add new vehicles in the showroom
2.Display and Sell selected vehicle
3.Number of that type of vehicles available
4.Search if that vehicle is available
5.Calculate profit
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct showroom
{
    char company[17];
    char name[17];
    int price;
    int quantity;
    int manucost;
    struct showroom*next;
};

void display(struct showroom *head)
{
    printf("Company\t\tName\t\tPrice\t\tQuantity\n");
    struct showroom*temp=head;      // O(1) and O(n)
        while(temp!=NULL)
        {
        printf("%s\t\t%s\t\t%d\t\t%d\n",temp->company,temp->name,temp->price,temp->quantity);
        temp=temp->next;
        }
}

struct showroom *create(struct showroom *head)
{
    head=(struct showroom*)malloc(sizeof(struct showroom));
    printf("Enter First vehicle company\n");
    scanf("%s",head->company);
    printf("Enter First vehicle name\n");
    scanf("%s",head->name);
    printf("Enter First vehicle manufacturing cost\n");
    scanf("%d",&head->manucost);
    printf("Enter First vehicle price\n");
    scanf("%d",&head->price);
    printf("Enter no.of vehicles of this type\n");
    scanf("%d",&head->quantity);
    head->next=NULL;

    struct showroom *temp=head;

    int ch;
    printf("\nEnter 1 to enter new vehicle and 0 to stop vehicle insertion\n");
    scanf("%d",&ch);
    printf("\n");
    int i=2;
    while(ch>0)     // O(1) and O(n)
    {
        struct showroom *newv=(struct showroom*)malloc(sizeof(struct showroom));
        printf("Enter vehicle %d company\n",i);
        scanf("%s",newv->company);
        printf("Enter vehicle %d name\n",i);
        scanf("%s",newv->name);
        printf("Enter vehicle manufacturing cost\n");
        scanf("%d",&newv->manucost);
        printf("Enter vehicle %d price\n",i);
        scanf("%d",&newv->price);
        printf("Enter no.of vehicles of this type %d added\n",i);
        scanf("%d",&newv->quantity);

        i++;
        newv->next=NULL;
        temp->next=newv;
        temp=newv;

        printf("\nEnter 1 to enter new vehicle and 0 to stop vehicle insertion\n");
        scanf("%d",&ch);
        printf("\n");
    }
    return head;
}

int search(struct showroom *head)
{
    struct showroom *newv=(struct showroom *)malloc(sizeof(struct showroom));
    struct showroom *temp=head;
    printf("\nEnter vehicle company\n");
    scanf("%s",newv->company);
    printf("Enter vehicle name\n");
    scanf("%s",newv->name);

    int i=0;
    while(temp!=NULL)           // O(1) and O(n^2)
    {
        i++;
        if(strcmp(temp->company,newv->company)==0 && strcmp(temp->name,newv->name)==0 && temp->quantity>0)
        {
            printf("\nYes,available\n");
            printf("Enter %d in sell option to sell\n",i);
            return 1;
        }
        temp=temp->next;
    }
    if(temp==NULL)
    {
        printf("\nNot Available\n");
        return 0;
    }
}

int sell(struct showroom *head)
{
    int profit=0;
    printf("\nIf the customer know what vehicle he want to buy,Press 1\nIf customer wants to buy what is available,Press 0\n");
    struct showroom *temp = head;
    int f;
    scanf("%d",&f);
    if(f==1)            // O(1) and O(n)
    {
      int k = search(head);
      if (k==0)
        return 0;
    }
    else
    display(head);
    
    int j,n;
    printf("Enter which vehicle to sell:\n");
    scanf("%d",&j);
    printf("Enter how many to sell\n");
    scanf("%d",&n); 
   
    
    for(int i=0;i<j-1;i++)
    {
    temp=temp->next;
    }
        if(temp->quantity>=n)
        {
        temp->quantity=temp->quantity-n;
        printf("The vechiles left are %d\n",temp->quantity);
        profit=(n) *((temp->price)-(temp->manucost));
        printf("Profit for this deal is: %d\n",profit);
        }
        else if(temp->quantity<n)
        {
        printf("Those many vehicles not available there are only %d left\n",temp->quantity);
        }
    return profit;    
}

void add(struct showroom *head)
{
    struct showroom *newv=(struct showroom *)malloc(sizeof(struct showroom));
    struct showroom *temp=head;
    struct showroom *prev=NULL;
    printf("Enter vehicle company\n");
    scanf("%s",newv->company);
    printf("Enter vehicle name\n");
    scanf("%s",newv->name);
    printf("Enter no.of vehicles of this type added\n");
    scanf("%d",&newv->quantity);
    
    while(temp!=NULL)           // O(1) and O(n^2)
    {
        if(strcmp(temp->company,newv->company)==0 && strcmp(temp->name,newv->name)==0)
        {
            temp->quantity=temp->quantity+newv->quantity;
            break;
        }
        prev=temp;
        temp=temp->next;
    }

    if(temp==NULL)
    {
        printf("Enter vehicle manufacturing cost\n");
        scanf("%d",&newv->manucost);
        printf("Enter vehicle price\n");
        scanf("%d",&newv->price);
        newv->next=NULL;
        prev->next=newv;
    }
}

int main()              // O(1)
{
    int bnet=0,cnet=0;
    struct showroom *chead, *bhead;
    printf("Enter all bike details available in the morning:\n");
    bhead=create(bhead);
    printf("Enter all car details available in the morning:\n");
    chead=create(chead);

    printf("\nEnter:\n1 to display\n2 to sell\n3 to add\n4 to calculate profit\n5 to exit\n");
    while(1)
    {
    printf("\nMake choice:\n");
    int a;
    scanf("%d",&a);
    switch(a)
    {
        case 1:
        {
            printf("Enter b or c:\n");
            char x;
            scanf(" %c",&x);
            if(x=='b')
            {
                display(bhead);
            }
            else if(x=='c')
            {
                display(chead);
            }
            break;
        }

        case 2:
        {
            printf("Enter b or c:\n");
            char x;
            scanf(" %c",&x);
            if(x=='b')
            {
                bnet=bnet+sell(bhead);
            }
            else if(x=='c')
            {
                cnet=cnet+sell(chead);
            }
            break;
        }

        case 3:
        {
            printf("Enter b or c:\n");
            char x;
            scanf(" %c",&x);
            if(x=='b')
            {
                add(bhead);
            }
            else if(x=='c')
            {
                add(chead);
            }
            break;   
        }

        case 4:
        {
            printf("\nTotal profit for the day=%d\n",cnet+bnet);
            break;
        }

        case 5:
        {
            return 0;
        }
    }
    }           // O(1) and O(n^2)
    return 0;
}