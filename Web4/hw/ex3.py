from river import River
import mlab

mlab.connect()

rivers_list = River.objects(length__lt = 1000)

for r in rivers_list:
    if r.continent == "S. America":
        print(r.name)
        print(r.continent)
        print(r.length)
        print("*    *    *    *     *    *")
