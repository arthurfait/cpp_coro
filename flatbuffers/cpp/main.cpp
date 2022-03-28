#include "demo_generated.h"

#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <iostream>

using namespace MyGame::Sample;

constexpr char kDataPath[] = "fl.dat";

void dump(uint8_t* buff, size_t size);

int main(int argc, char const *argv[])
{
    if (argc > 1 && strncmp(argv[1], "read", 4) == 0) {
        int fd = open(kDataPath, O_RDONLY);
        if (fd != -1) {
            auto size = lseek(fd, 0, SEEK_END);
            lseek(fd, 0, SEEK_SET);
            std::vector<uint8_t> vec(size);
            int r = read(fd, vec.data(), size);
            close(fd);
            auto entity = GetMonster(vec.data());
            std::cout << "Monster name: " << entity->name()->c_str() << "\n";
            std::cout << "Monster hp: " << entity->hp() << "\n";
        }
        return 0;
    }

    flatbuffers::FlatBufferBuilder builder(91024);
    auto weapon = builder.CreateString("Axe");
    short weapon_damage = 3;

    auto weapon_sword = builder.CreateString("Sword");
    short weapon_sword_damage = 6;

    auto axe = CreateWeapon(builder, weapon, weapon_damage);
    auto sword = CreateWeapon(builder, weapon_sword, weapon_sword_damage);


    auto name = builder.CreateString("orc");
    unsigned char treasure[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    auto inventory = builder.CreateVector(treasure, 10);

    // Place the weapons into a `std::vector`, then convert that into a FlatBuffer `vector`.
    std::vector<flatbuffers::Offset<Weapon>> weapons_vector;
    weapons_vector.push_back(sword);
    weapons_vector.push_back(axe);
    auto weapons = builder.CreateVector(weapons_vector);

    Vec3 points[] = { Vec3(1.0f, 2.0f, 3.0f), Vec3(4.0f, 5.0f, 6.0f) };
    auto path = builder.CreateVectorOfStructs(points, 2);

    auto position = Vec3(1.0f, 2.0f, 3.0f);

    int hp = 300;
    int mana = 150;

    auto orc = CreateMonster(builder, &position, mana, hp, name, inventory,
                        Color_Red, weapons, Equipment_Weapon, axe.Union(),
                        path);


    builder.Finish(orc);

    uint8_t *buf = builder.GetBufferPointer();
    auto size = builder.GetSize(); // Returns the size of the buffer that

    dump(buf, size);


    return 0;
}


void dump(uint8_t* buff, size_t size)
{
    int fd = open(kDataPath, O_WRONLY | O_CREAT | O_TRUNC, 0600);
    if (fd != -1) {
        write(fd, buff, size);
        close(fd);
    }
}