import py621


def testMD5():
    assert py621.public.genmd5(
        "tests/md5test.jpg") == "55dff350e4d5f5a7602bc3dffc78e21a"


def testPost():
    api = py621.public.apiGet(py621.types.e926)
    tags = ["id:2685595"]
    SamplePosts = api.getPosts(tags, 10, 1, False)
    SamplePost = SamplePosts[0]
    assert SamplePost.id == 2685595
    assert SamplePost.file.url == "https://static1.e926.net/data/5e/02/5e02da74041ac235f616f11a0e68802f.jpg"


def testPool():
    api = py621.public.apiGet(py621.types.e621)
    pool = api.getPool(6527)
    SamplePosts = pool.getPosts()
    SamplePost = SamplePosts[0]
    assert SamplePost.id == 698919
    assert SamplePost.file.url == "https://static1.e621.net/data/58/81/58819b4b6a59154da2c1a58e950a3d12.png"
