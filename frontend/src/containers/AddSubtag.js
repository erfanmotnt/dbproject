import React, { useState, useRef } from 'react'
import {
  Container,
  Grid,
  makeStyles,
  TextField,
  Button,
  Typography,
  Paper,
  Select,
} from '@material-ui/core';
import { toast } from 'react-toastify';
import { connect } from 'react-redux';
import { createSubtag } from '../redux/actions/properties';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    direction: 'ltr',
  },
  background: {
    minHeight: `calc(100vh - 5em)`,
  },
  title: {
    fontSize: 40,
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    margin: 'auto',
  },
}))

const Subtag = ({ createSubtag }) => {
  const classes = useStyles();
  const [subtagName, setSubtagName] = useState('')
  const [tagName, setTagName] = useState('')

  const handleSubmit = () => {
    if (!subtagName || !tagName) {
      toast.error('لطفاً هم عنوان ساب‌تگ و هم عنوان تگ پدر را وارد کن!');
      return;
    }
    createSubtag(subtagName, tagName)
  }

  return (
    <div className={classes.root}>
      <Grid container justify='center' alignItems='center' className={classes.background}>
        <Grid
          xs={10}
          sm={6}
          item container
          justify='center'
          alignItems='stretch'
          direction='column'
          spacing={6}>
          <Grid item>
            <Typography gutterBottom variant='h3' className={classes.title} align='center'>
              افزودن ساب‌تگ
            </Typography>
          </Grid>
          <Grid item >
            <Paper className={classes.paper}>
              <Grid
                container
                direction='column'
                justify='center'
                spacing={2}>
                <Grid item>
                  <TextField
                    label='عنوان ساب‌تگ'
                    variant='outlined'
                    gutterBottom
                    fullWidth
                    onChange={(e) => setSubtagName(e.target.value)}
                  />
                </Grid>
                <Grid item>
                  <TextField
                    label='عنوان تگ پدر'
                    variant='outlined'
                    gutterBottom
                    fullWidth
                    onChange={(e) => setTagName(e.target.value)}
                  />
                </Grid>
                <Grid container item alignItems='center' justify='center' spacing={2}>
                  <Grid item>
                    <Button
                      variant='contained'
                      color='primary'
                      onClick={handleSubmit}
                    >
                      بزن بریم
                    </Button>
                  </Grid>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
        </Grid>
      </Grid>
    </div>
  )
}

const mapStateToProps = (state, ownProps) => ({

})

export default connect(
  mapStateToProps,
  {
    createSubtag,
  }
)(Subtag);