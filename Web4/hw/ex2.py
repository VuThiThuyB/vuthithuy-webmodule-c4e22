from river import River
import mlab

mlab.connect()

rivers_list = River.objects()

for r in rivers_list:
    if r.continent== "Africa":
        print(r.name)
        print(r.continent)
        print(r.length)
        print("*   *    *   *   *    *    *   *")
