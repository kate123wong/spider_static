#include<windows.h>


// 人的方向
typedef enum _dirction
{
	PERSON_UP,
	PERSON_DOWN,
	PERSON_LEFT,
	PERSON_RIGHT,
}dirction;



// 游戏坐标
typedef struct _GAME_COORD
{
	short x;
	short y;
}GAME_COORD, *PGAME_COORD;


/// game_opration.c 中的接口函数


void OnKeyDown(DWORD vk);
