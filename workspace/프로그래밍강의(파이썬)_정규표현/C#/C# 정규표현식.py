# C#으로 정규표현식을 다룰 때에는 Regex.matches라는 메소드를 이용합니다.
#
# 주의할 점: C#에서는 \ 대신 \\를 적어야 합니다.
#
# Python은 raw string을 지원해 대표 문자1를 표현할 때 역슬래시 \ 를 한 번만 쓸 수 있습니다. 허나, C#에서는 escape 때문에 역슬래시를 사용해 역슬래시 \를 두 번 적어야 합니다.

using System;
using System.Text.Regusing System;
using System.Text.RegularExpressions;

public class RegexTest {
    public static void Main() {
        string regex = "\d";

        string searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        foreach (Match m in Regex.Matches(searchTarget, regex)){
            Console.WriteLine(m.Value);
        }
    }
}