def generate_swizzle_vec2(arr, result):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            result['{}{}'.format(arr[i], arr[j])] = """@property
def {}{}(self):
    return vec2.Vec2(self.{}, self.{})
""".format(arr[i], arr[j], arr[i], arr[j])
            if i != j:
                result['{}{}_setter'.format(arr[i], arr[j])] = """@{}{}.setter
def {}{}(self, value):
    self.{} = value[0]
    self.{} = value[1]
""".format(arr[i], arr[j], arr[i], arr[j], arr[i], arr[j])


def generate_swizzle_vec3(arr, result):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            for k in range(0, len(arr)):
                result['{}{}{}'.format(arr[i], arr[j], arr[k])] = """@property
def {}{}{}(self):
    return vec3.Vec3(self.{}, self.{}, self.{})
""".format(arr[i], arr[j], arr[k], arr[i], arr[j], arr[k])
                if i != j and j != k and i != k:
                    result['{}{}{}_setter'.format(arr[i], arr[j], arr[k])] = """@{}{}{}.setter
def {}{}{}(self, value):
    self.{} = value[0]
    self.{} = value[1]
    self.{} = value[2]
""".format(arr[i], arr[j], arr[k], arr[i], arr[j], arr[k], arr[i], arr[j], arr[k])

v = 1
if v == 0:
    result = {}
    generate_swizzle_vec2(['x', 'y'], result)
    for k in sorted(result):
        print result[k]
elif v == 1:
    result = {}
    generate_swizzle_vec2(['x', 'y'], result)
    generate_swizzle_vec2(['x', 'z'], result)
    generate_swizzle_vec2(['y', 'z'], result)
    generate_swizzle_vec3(['x', 'y', 'z'], result)
    for k in sorted(result):
        print result[k]
