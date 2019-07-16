
/************** 头文件 ****************/
#include<windows.h>
#include "Sokoban.h"

// 当用于操作时进行的逻辑处理。
// 本游戏只使用到了键盘上下左右键控制。
void OnKeyDown(DWORD vk)
{
	switch (vk) // virtual key value
	{
	case VK_LEFT:
		MoveTo(PERSON_LEFT);
		break;
	case VK_RIGHT:
		MoveTo(PERSON_RIGHT);
		break;
	case VK_UP:
		MoveTo(PERSON_UP);
		break;
	case VK_DOWN:
		MoveTo(PERSON_DOWN);
		break;
	}
	return;
}

// 游戏的初始化，
// 创建游戏的内部数据结构和系统对象。
void CreateGame(HWND hwnd, // 主窗口句柄
	dirction init_dir)
{
	// 创建表示箱子的数据结构
	CreateBox();

    //创建目的地箱子
    CreataFlagBoxs();

	// 创建表示地图的数据结构
	CreateMap();
}
//mvc