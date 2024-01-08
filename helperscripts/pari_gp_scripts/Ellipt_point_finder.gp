
setCurveParameters(bitLength) =
{
  while(1,
    p = 2^(bitLength-1) + 2*random(2^(bitLength-3)) + 1;
    if(isprime(p), break);
  );

  abFlag = 0;
  until(abFlag,
    a = 0;
    until(a,
      a = random(2^(bitLength-1));
      if((a < 1) || (a > p-1),
        a = 0;
      );
    );

    b = 0;
    until(b,
      b = random(2^(bitLength-1));
      if((b < 1) || (b > p-1),
        b = 0;
      );
    );

    if(Mod(4*a^3 + 27*b^2, p),
      abFlag = 1;
    );
  );

  E = ellinit([a, b], p);

  return(E);
}



findPointsOfPrimeOrder(E, bitLength) =
{
  p = E.a1.mod;
  a = lift(E.a4);
  b = lift(E.a6);
  n_total = 0;
  n_good = 0;
  for(x=0, p-1,
    s = Mod(x^3 + a*x + b, p);
    if(lift(s^((p-1)/2)) == 1,
      n_total ++;
      if(n_total > bitLength,
        if(n_good/n_total < 0.5,
          return(0);
        );
      );
      y = lift(s^(1/2));
      ord = ellorder(E, [x,y]);
      if(isprime(ord),
        n_good ++;
        print("a=", a, " b=", b, " p=", p, " P=[", x, ", ", y, "]", " ord=", ord);
      );
    );
  );
  return(1);
}



findPointsOfPrimeOrderComplete(E) =
{
  p = E.a1.mod;
  a = lift(E.a4);
  b = lift(E.a6);
  for(x=0, p-1,
    s = Mod(x^3 + a*x + b, p);
    if(lift(s^((p-1)/2)) == 1,
      y = lift(s^(1/2));
      ord = ellorder(E, [x,y]);
      if(isprime(ord),
        print("a=", a, " b=", b, " p=", p, " P=[", x, ", ", y, "]", " ord=", ord);
      );
    );
  );
}



searchExample(bitLength) =
{
  a = 0;
  until(a,
    E = setCurveParameters(bitLength);
    a = findPointsOfPrimeOrder(E, bitLength);
  );
}

\\RUN THIS SCRIPT WITH gp -f -s 80M -q Ellipt_point_finder.gp OTHERWISE YOU GET A STACKOVERFLOW

\\CHANGE THIS PARAMETER

bitLength = 256

\\END OF CHANGE
searchExample(bitLength);
