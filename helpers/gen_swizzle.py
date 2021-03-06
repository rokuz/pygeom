def generate_header_vec2():
    return """# Generated by {}. Do not modify.
import vec2


class GenVec2(object):
    def __init__(self, x, y):
        self.x = 1.0 * x
        self.y = 1.0 * y\n\n""".format(__file__[str(__file__).rfind('pygeom'):])


def generate_header_vec3():
    return """# Generated by {}. Do not modify.
import vec2
import vec3


class GenVec3(object):
    def __init__(self, x, y, z):
        self.x = 1.0 * x
        self.y = 1.0 * y
        self.z = 1.0 * z\n\n""".format(__file__[str(__file__).rfind('pygeom'):])


def generate_swizzle_vec2(arr, result):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            result['{}{}'.format(arr[i], arr[j])] = """    @property
    def {0}{1}(self):
        return vec2.Vec2(self.{0}, self.{1})\n\n""".format(arr[i], arr[j])
            if i != j:
                result['{}{}_setter'.format(arr[i], arr[j])] = """    @{0}{1}.setter
    def {0}{1}(self, value):
        self.{0} = value[0]
        self.{1} = value[1]\n\n""".format(arr[i], arr[j])


def generate_swizzle_vec3(arr, result):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            for k in range(0, len(arr)):
                result['{}{}{}'.format(arr[i], arr[j], arr[k])] = """    @property
    def {0}{1}{2}(self):
        return vec3.Vec3(self.{0}, self.{1}, self.{2})\n\n""".format(arr[i], arr[j], arr[k])
                if i != j and j != k and i != k:
                    result['{}{}{}_setter'.format(arr[i], arr[j], arr[k])] = """    @{0}{1}{2}.setter
    def {0}{1}{2}(self, value):
        self.{0} = value[0]
        self.{1} = value[1]
        self.{2} = value[2]\n\n""".format(arr[i], arr[j], arr[k])


with open("../vec2_gen.py", "w") as f:
    f.write(generate_header_vec2())
    result = {}
    generate_swizzle_vec2(['x', 'y'], result)
    cnt = 1
    for k in sorted(result):
        v = result[k]
        f.write(v if cnt != len(result) else v[0:-1])
        cnt += 1

with open("../vec3_gen.py", "w") as f:
    f.write(generate_header_vec3())
    result = {}
    generate_swizzle_vec2(['x', 'y'], result)
    generate_swizzle_vec2(['x', 'z'], result)
    generate_swizzle_vec2(['y', 'z'], result)
    generate_swizzle_vec3(['x', 'y', 'z'], result)
    cnt = 1
    for k in sorted(result):
        v = result[k]
        f.write(v if cnt != len(result) else v[0:-1])
        cnt += 1
