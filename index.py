import optparse

def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = optparse.OptionParser(usage=usage)

    parser.add_option(
        # option
        '-f', '--file',
        # parser にどんな動作をさせたいか
        action='store',
        # 引数の型
        type='string',
        # optparse に知らせる action の値の格納場所
        dest='filename',
        # --help 実行時の説明文
        help='sample descritption about the -f option.'
    )

    parser.add_option(
        '-n', '--num',
        action='store',
        type='int',
        dest='num',
        help='sample descritption for -n option.'
    )

    parser.add_option(
        '-v', '--verbose',
        action='store_false',
        # type を指定したら怒られた
        # type='bool',
        dest='verbose',
        help='sample descritption for -v option.',
        default=True
    )

    # unpack touple
    options, args = parser.parse_args()
    print(options)
    print(args)

if __name__ == '__main__':
    main()
